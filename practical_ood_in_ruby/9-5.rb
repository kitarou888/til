class Mechanic
  def prepare_bicycle(bicycle)

  end
end

class TripCoordinator
  def buy_food(customers)

  end
end

class Driver
  def gas_up(vehicle)

  end
  def fill_water_tank(vehicle)

  end
end

class Trip
  attr_reader :bicycle, :customers, :vehicle

  def prepare(prepares)
    prepares.each {|preparer|
      case preparer
      when Mechanic
        preparer.prepare_bicycle(bicycles)
      when TripCoordinator
        preparer.buy_food(customers)
      when Driver
        preparer.gas_up(vehicle)
        preparer.fill_water_tank(vehicle)
      end
    }
  end
end
