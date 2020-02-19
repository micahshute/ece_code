require 'pry'
require 'ipaddr'

class IPGen

    def self.ip4
        IPAddr.new(rand(2 ** 32), Socket::AF_INET).to_s
    end

end

class GraphNode

    attr_reader :value, :connections

    def initialize(value, connections = [])
        @value, @connections = value, connections
    end

    def neighbors
        self.connections.map{ |conn| conn.dest(self) }
    end

    def neighbor(conn)
        conn.dest(self)
    end

    def go_to(neighbor)
        conn = self.connections.find{ |c| c.dest(self) == neighbor }
        raise ArgumentError.new("Neighbor must be connected") if !conn
        conn.traverse_from(self) { |len| yield(len) if block_given? }
    end

end

class GraphEdge

    attr_accessor :length

    def initialize(node1, node2, length)
        @node1, @node2, @length = node1, node2, length
        @node1.connections << self
        @node2.connections << self
    end

    def dest(start)
        raise ArgumentError.new("Argument must be a node in the connection") if start != @node1 && start != @node2
        return start == @node1 ? @node2 : @node1
    end 

    def traverse_from(start)
        yield @length if block_given?
        return dest(start)
    end

end

module DNSServerMethods

    @@tlds = ["com", "net", "edu", "gov"]

    def get_domain(server_name)
        server_name.match(/[^.]+.#{get_tld(server_name)}/).to_s[0...-4]
    end

    def get_tld(server_name)
        @@tlds.each do |tld|
            return tld if server_name.include?(tld)
        end
        raise StandardError.new("TLD not included in URL")
    end

    def tld_servername_for(tld)
        "tld-#{tld}.net"
    end

    def dns_servername_for(domain, tld)
        "dns-#{domain}.#{tld}"
    end
end


class Website

    include DNSServerMethods

    @@all = []

    def self.all
        @@all
    end

    

    def self.from_ip(ip)
        @@all.find{ |w| w.ip == ip}
    end

    attr_accessor :url, :ip, :comm_listener, :connections


    def initialize(url, ip = IPGen.ip4)
        @url, @ip, @connections = url, ip, []
        @@all << self
    end

    def name
        @url
    end

    def open_connection(client: , comm_listener: nil, type: nil, priority: 1)
        if (comm = @connections.find{ |c| c[:client] == client })
            # just get request
            comm[:comm_listener][self, priority] # get-res
            priority += 1
        else
            @connections << {client: client, comm_listener: comm_listener} if type == :persistent
            if comm_listener
                comm_listener[self, priority] # syn-synack
                priority += 1
                comm_listener[self, priority] # ack_get-res
                priority += 1
            end
        end
        return priority
    end

end



class DNSServer

    include DNSServerMethods

    @@all = []

    def self.all
        @@all
    end

    def self.root
        @@all.select{ |dns| dns.name.include?("root") }
    end

    def self.tlds
        @@all.select{ |dns| dns.name.include?("tld")}
    end

    def self.from_ip(ip)
        @@all.find{ |s| s.ip == ip }
    end

    #query_listener is a lamda that is called during recurisve_queries to keep track of RTTs
    attr_accessor :name, :cache, :ip, :query_listener

    def initialize(name, cache, ip = IPGen.ip4)
        @name, @cache, @ip = name, cache, ip
        @@all << self
    end

    def recursive_query(website_name, priority = 1)
        check_cache = self.a_query(website_name)
        step = priority
        while !check_cache.is_a?(Website)
            @query_listener[check_cache, step] if @query_listener
            step += 1
            check_cache = check_cache.a_query(website_name)
            self.cache[check_cache.name] = check_cache.ip #if !check_cache.is_a?(Website)
        end
        return {res: check_cache, step: step}
    end

    def a_query(website)
        begin
            return find_server_in_cache(website)     
        rescue
            begin 
                return dns_server_for(website)
            rescue
                begin
                    return tld_server_for(website)
                rescue
                    return root_server
                end
            end
        end
    end

    private

    def dns_server_for(name)
        servername = dns_servername_for(get_domain(name), get_tld(name))
        find_server_in_cache(servername)
    end

    def tld_server_for(name)
        servername = tld_servername_for(get_tld(name))
        find_server_in_cache(servername)
    end
    
    def root_server
        find_server_in_cache("a.root-servers.net")
    end

    def find_server_in_cache(servername)
        server_ip = cache[servername]
        raise StandardError.new("DNS server does not have #{servername}") if !server_ip
        return self.class.from_ip(server_ip) || Website.from_ip(server_ip)
    end
end

class DNSFactory

    extend DNSServerMethods

    def self.dns_network_from_websites(websites)
        domains = websites.map{ |w| get_domain(w.name) }.uniq
        dns_domain_servers = domains.map do |domain| 
            sites = websites.select{ |w| get_domain(w.name) == domain}
            tlds = sites.map{ |s| get_tld(s.name) }.uniq
            tlds.map do |tld|
                tld_sites = sites.select{ |s| get_tld(s.name) == tld }
                cache = tld_sites.each_with_object({}){ |site, cache| cache[site.name] = site.ip }
                DNSServer.new(dns_servername_for(domain, tld), cache)
            end
        end.flatten
        make_tld_servers(dns_domain_servers)
        local_dns_server = DNSServer.new("Local", {})
        make_root_server
        local_dns_server
    end

    def self.create(server_name_cache_hash)
        server_name_cache_hash.each do |server, cache|
            DNSServer.new(server, cache)
        end
    end

    private

    def self.make_tld_servers(server_objs)
        tlds = server_objs.map{ |s| get_tld(s.name) }.uniq
        tlds.map do |tld|
            dns_servers_of_tld = server_objs.select{ |s| get_tld(s.name) == tld }
            tld_cache = dns_servers_of_tld.each_with_object({}){ |s, cache| cache[s.name] = s.ip }
            DNSServer.new(tld_servername_for(tld), tld_cache)
        end
    end

    def self.make_root_server
        root_cache = DNSServer.tlds.each_with_object({}){ |s, cache| cache[s.name] = s.ip }
        root = DNSServer.new("a.root-servers.net", root_cache)
        DNSServer.all.each { |s| s.cache[root.name] = root.ip }
        root
    end

end


class TimingSimulator

    attr_accessor :serial_threads, :parallel_threads, :start, :stop, :tasks, :current

    def initialize
        @serial_thread, @parallel_threads, @tasks, @current = nil, [], [], 0
    end

    def start_sim
        @start = Time.now
    end

    def new_parallel_task(lam)
        @parallel_threads << Thread.new{ lam[] }
    end

    def new_task(lam)
        if !@serial_thread || !@serial_thread.alive?
            @serial_thread = Thread.new do
                @current = lam[:priority] if lam[:priority]
                lam[:proc][]
                while @tasks.length > 0
                    task = @tasks.shift
                    @current = task[:priority] if task[:priority]
                    while @tasks[0] && @tasks[0][:priority] <= @current
                        new_parallel_task(@tasks.shift[:proc])
                    end
                    task[:proc][]
                end
            end
        else
            if lam[:priority] <= @current
                new_parallel_task(lam[:proc])
            else
                @tasks << lam
                @tasks.sort!{ |a,b| a[:priority] <=> b[:priority]}
            end
        end
    end

    def new_serial_task(lam)
        if !@serial_thread || !@serial_thread.alive?
            @serial_thread = Thread.new do
                @current = lam[:priority]
                lam[:proc][]
                while @tasks.length > 0
                    task = @tasks.shift
                    lam[:priority]
                    task[:proc][]
                end
            end
        else
            @tasks << lam
        end
    end

    def end_sim
        while @tasks.length > 0
            @serial_thread.join if @serial_thread
        end
        @serial_thread.join if @serial_thread
        @parallel_threads.each(&:join)
        @stop = Time.now
        @stop - @start
    end


end


# RTT = 1
# client = IPGen.ip4
# cnn = Website.new("www.cnn.com")
# pics_cnn = Website.new("www.pics.cnn.com")
# google = Website.new("www.google.com")

# local = DNSFactory.dns_network_from_websites([cnn, pics_cnn, google])

# graph_nodes = DNSServer.all.map{ |server| GraphNode.new(server) }
# graph_nodes.concat(Website.all.map{ |server| GraphNode.new(server) })
# graph_nodes << GraphNode.new(client)
# graph_nodes.each do |gn1|
#     graph_nodes.each do |gn2|
#         if gn1 != gn2 && !gn1.neighbors.include?(gn2)
#             GraphEdge.new(gn1, gn2, RTT)
#         end
#     end
# end





# tot_rtts = 0
# local.query_listener = ->(a){ 
#     node = graph_nodes.find{ |gn| gn.value == a } 
#     local_node = graph_nodes.find{ |gn| gn.value == local }
#     puts "Going from #{local.name} to #{a.name} and back"
#     local_node.go_to(node) do |len|
#         tot_rtts += len
#     end
# }


# sim = TimingSimulator.new

# sim.start_sim
# local.query_listener = ->(a, step){ 
#     node = graph_nodes.find{ |gn| gn.value == a } 
#     local_node = graph_nodes.find{ |gn| gn.value == local }
#     local_node.go_to(node) do |len|
#         sim.new_task( {proc: ->(){ puts "Going from #{local.name} to #{a.name} and back";  sleep(len)}, priority: step } )
#     end
# }

# tcp_listener = ->(site, step){
#     node = graph_nodes.find{ |gn| gn.value == site } 
#     client_node = graph_nodes.find{ |gn| gn.value == client }
#     client_node.go_to(node) do |len|
#         sim.new_task( {proc: ->(){ puts "Going from client to #{site.name} and back"; sleep(len)}, priority: step } )
#     end
# }

# Make priorities incremental so everything happens in series

# get_cnn_ip = local.recursive_query("www.cnn.com")
# complete_conn_to_cnn = get_cnn_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: nil, priority: get_cnn_ip[:step] )
# get_pics_cnn_ip = local.recursive_query("www.pics.cnn.com", complete_conn_to_cnn)
# complete_conn_to_pics_cnn = get_pics_cnn_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: nil, priority: get_pics_cnn_ip[:step])
# get_google_ip = local.recursive_query("www.google.com", complete_conn_to_pics_cnn)
# get_google_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: nil, priority: get_google_ip[:step])

# puts "TOTAL RTT: #{sim.end_sim.round}"


# get_cnn_ip = local.recursive_query("www.cnn.com")
# complete_conn_to_cnn = get_cnn_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: :persistent, priority: get_cnn_ip[:step] )
# get_pics_cnn_ip = local.recursive_query("www.pics.cnn.com", complete_conn_to_cnn)
# complete_conn_to_pics_cnn = get_pics_cnn_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: :persistent, priority: get_pics_cnn_ip[:step])
# get_google_ip = local.recursive_query("www.google.com", complete_conn_to_cnn)
# get_google_ip[:res].open_connection(client: client, comm_listener: tcp_listener, type: nil, priority: get_google_ip[:step])

# puts "TOTAL RTT: #{sim.end_sim.round}"

class P2PNode
    
    attr_accessor :name, :files, :query_listener, :seen_query

    def initialize(name, files = [])
        @name = name
        @files = files
        @seen_query = 0
    end


    def receive_file(file)
        @files << file
    end

    def query(query, node_ref)
        return if query.id <= @seen_query
        if self.have_file?(query.filename)
            puts "Sending #{query.filename} to #{query.sender.name}"
            query.sender.receive_file(query.filename)
            return
        end
    
        query.ttl -= 1
        @seen_query = query.id
        query_listener[query, node_ref] if query.ttl > 0
    end

    def have_file?(file)
        @files.include?(file)
    end
    
end

class P2PQuery

    @@id = 1

    attr_accessor :ttl, :filename, :id, :sender

    def initialize(filename:, ttl:, sender: )
        @ttl, @filename, @id, @sender = ttl, filename, @@id, sender
        @@id += 1
    end
    
end


nodes = ["A", "B", "C", "D", "E"]
nodes.map!{ |n| P2PNode.new(n) }
nodes.last.files << "file.txt"
p2pnodes = nodes.dup
nodes.map!{ |n| GraphNode.new(n) }

GraphEdge.new(nodes[0], nodes[1], 1)
GraphEdge.new(nodes[1], nodes[2], 1)
GraphEdge.new(nodes[2], nodes[3], 1)
GraphEdge.new(nodes[3], nodes[4], 1)
total_transmissions = 0

query_listener = ->(query, node){
    node.neighbors.each do |n|
        total_transmissions += 1
        puts "Transmitting from #{node.value.name} to #{n.value.name}"
        n.value.query(query, n)
    end
}

p2pnodes.each { |n| n.query_listener = query_listener }

a = nodes.first
a_files = a.value.files.length
ttl = 0
while a_files >= a.value.files.length
    ttl += 1
    query = P2PQuery.new(filename: "file.txt", ttl: ttl, sender: a.value)
    a.value.seen_query = query.id
    a.neighbors.each do |n|
        puts "Transmitting from #{a.value.name} to #{n.value.name}"
        total_transmissions += 1
        n.value.query(query, n)
    end
end
puts "Total Transmissions: #{total_transmissions}"
binding.pry