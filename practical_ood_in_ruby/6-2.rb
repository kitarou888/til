class Bicycle
  attr_reader :size, :chain, :tire_size

  def initialize(args={})
    @size = args[:size]
    @chain = args[:chain] || default_chain
    @tire_size = args[:tire_size] || default_tire_size

    post_initialize(args) # Bicycleでは送信と・・・
  end

  def post_initialize(args) # ・・・実装の両方を行う
    nil
  end

  def spares
    { tire_size: tire_size,
      chain: chain }
  end

  def default_chain # <- 共通の初期値
    '10-speed'
  end

  def default_tire_size
    raise NotImplementedError, "This #{self.class} cannot respond to:"
  end
end

class RoadBike < Bicycle
  attr_reader :tape_color

  def post_initialize(args) # RoadBikeは任意でオーバーライドできる
    @tape_color = args[:tape_color]
  end

  def spares
    super.merge({ tape_color: tape_color })
  end

  def default_tire_size # <- サブクラスの初期値
    '23'
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

  def default_tire_size # <- サブクラスの初期値
    '2.1'
  end
end

class RecumbentBike < Bicycle
  attr_reader :flag

  def initialize(args)
    @flag = args[:flag] # 'super'を送信するのを忘れた
  end

  def spares
    super.merge({ flag: flag })
  end

  def default_chain
    '9-speed'
  end

  def default_tire_size
    '28'
  end
end

road_bike = RoadBike.new(size: 'M', tape_color: 'red')
p road_bike.size
p road_bike.spares
p road_bike.tire_size
p road_bike.chain

mountain_bike = MountainBike.new(size: 'S', front_shock: 'Manitou', rear_shock: 'Fox')
p mountain_bike.size
p mountain_bike.spares
p mountain_bike.tire_size
p mountain_bike.chain

bent_bike = RecumbentBike.new(flag: 'tall and orange')
p bent_bike.spares
