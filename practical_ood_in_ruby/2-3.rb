class RevealingReferences
  attr_reader :wheel
  def initialize(data)
    @wheels = wheelify(data)
  end

  # 最初に - 配列を繰り返し処理する
  def diameters
    wheels.collect {|wheel| diameter(wheel)}
  end

  # 次に - 「１つ」の車輪の直径を計算する
  def diameter(wheel)
    wheel.rim + (wheel.tire * 2)
  end

  Wheel = Struct.new(:rim, :tire)
  def wheelify(data)
    data.collect {|cell| Wheel.new(cell[0], cell[1])}
  end
end
