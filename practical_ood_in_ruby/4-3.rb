class Customer
  def initialize(on_date, of_difficulty, need_bike, trip)
    @on_date = on_date
    @of_difficulty = of_difficulty
    @need_bike = need_bike
    @trip = trip
  end
end

class TripFinder
  def initialize(trip, bike)
    @trip = trip
    @bike = bike
  end

  def suitable_trips(on_date, of_difficulty, need_bike)
    trips = trip.suitable_trips(on_date, of_difficulty)

    trips.each do |trip|
      bike.suitable_bicycle(trip_date, route_type)
    end
  end
end

class Trip
  def initialize(mechanic)
    @mechanic = mechanic
  end

  def suitable_trips(on_date, of_difficulty)
    ["tripA", "tripB"]
  end

  def bicycles
    ["bikeA", "bikeB", "bikeC"]
  end

  def prepare_trip(self)

  end
end

class Bicycle
  def suitable_bicycle(trip_date, route_type)
    ["bikeA", "bikeB"]
  end
end

class Mechanic
  def prepare_bicycle(trip)
    trip.bicycles.each do |bike|
      clean_bicycle(bike)
      pump_tires(bike)
      lube_chain(bike)
      check_brakes(bike)
    end
  end

  def clean_bicycle(bike)
  end

  def pump_tires(bike)
  end

  def lube_chain(bike)
  end

  def check_brakes(bike)
  end
end

Trip.new().suitable_trips(10, true, true)
