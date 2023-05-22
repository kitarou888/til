class Gate
  attr_accessor :name

  STATIONS = [:umeda, :juso, :mikuni]
  FARES = [160, 190]

  def initialize(name)
    @name = name
  end

  def enter(ticket)
    ticket.departure = @name
  end

  def exit(ticket)
    departure = ticket.stamp_at
    distance = (STATIONS.index(self.name) - STATIONS.index(ticket.departure)).abs
    
    if FARES.index(ticket.price) >= distance - 1
      true
    else
      false
    end
  end
end
