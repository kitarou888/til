class Ticket
  attr_accessor :price, :departure
  
  def initialize(price)
    @price = price
    @departure = nil
  end

  def stamp(name)
    @departure = name
  end

  def stamp_at
    self.departure
  end
end
