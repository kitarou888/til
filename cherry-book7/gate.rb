class Gate
  attr_accessor :name
  def initialize(name)
    @name = name
  end

  def enter(ticket)
    ticket.departure = @name
  end

  def exit(ticket)
    gates = [:umeda, :juso, :mikuni]
    departure = ticket.stamp_at
    distance = (gates.index(self.name) - gates.index(ticket.departure)).abs
    
    if ticket.price >= 160 && distance == 1
      true
    elsif ticket.price >= 190 && distance == 2
      true
    else
      false
    end
  end
end
