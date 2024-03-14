class Customer
  def initialize(on_date, of_difficulty, need_bike, trip)
    @on_date = on_date
    @of_difficulty = of_difficulty
    @need_bike = need_bike
    @trip = trip
  end
end

class Trip
  def suitable_trips(on_date, of_difficulty)
    ["tripA", "tripB"]
  end
end

class Bicycle
  def suitable_bicycle(trip_date, route_type)
    ["bikeA", "bikeB"]
  end
end

Trip.new().suitable_trips(10, true, true)
