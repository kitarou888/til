class Bicycle
  attr_reader :style, :size, :tape_color, :front_shock, :rear_shock

  def initialize(args)
    @style = args[:style]
    @size = args[:size]
    @tape_color = args[:tape_color]
    @front_shock = args[:front_shock]
    @rear_shock = args[:rear_shock]
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

bike1 = Bicycle.new(
  style: :road,
  size: "M",
  tape_color: "red"
)
bike2 = Bicycle.new(
  style: :mountain,
  size: "S",
  front_shock: "Manitou",
  rear_shock: "Fox"
)
bike2.spares
# -> { :tire_size => "2.1",
#      :chain => "10-speed",
#      :rear_shock => "Fox" }
