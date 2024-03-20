class Bicycle
  attr_reader :size # RoadBikeから昇格

  def initialize(args={})
    @size = args[:size] # Roadbikeから昇格
  end
end

class RoadBike < Bicycle
  attr_reader :tape_color

  def initialize(args)
    @tape_color = args[:tape_color]
    super(args) # RoadBikeはsuperを必ず呼ばなければならなくなった
  end

  # styleの確認は危険な道へ進む一歩
  def spares
    if style == :road
      { chain: "10-speed",
        tire_size: "23",
        tape_color: tape_color }
    else
      { chain: "10-speed",
        tire_size: "2.1",
        rear_shock: rear_shock }
    end
  end
end

class MountainBike < Bicycle
  attr_reader :front_shock, :rear_shock

  def initialize(args)
    @front_shock = args[:front_shock]
    @rear_shock = args[:rear_shock]
    super(args)
  end

  def spares
    super.merge(rear_shock: rear_shock)
  end
end

road_bike = RoadBike.new(size: 'M', tape_color: 'red')
p road_bike.size

mountain_bike = MountainBike.new(size: 'S', front_shock: 'Manitou', rear_shock: 'Fox')
p mountain_bike.size
p mountain_bike.spares
# -> { :tire_size => "2.1",
#      :chain => "10-speed",
#      :rear_shock => "Fox" }
