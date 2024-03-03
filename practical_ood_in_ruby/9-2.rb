require 'test/unit'

class Wheel
  attr_reader :rim, :tire
  def initialize(rim, tire)
    @rim = rim
    @tire = tire
  end

  def width
    rim + (tire * 2)
  end
end

class Gear
  attr_reader :chainring, :cog, :wheel
  def initialize(args)
    @chainring = args[:chainring]
    @cog = args[:cog]
    @wheel = args[:wheel]
  end

  def gear_inches
    # wheel 変数内のオブジェクトがDiameterizableロールを担う
    ratio * wheel.diameter # <--古くなっている！
  end

  def ratio
    chainring / cog.to_f
  end
end

class Diameterizable # diameterロールの担い手をつくる
  def diameter
    10
  end
end

class  WheelTest < Test::Unit::TestCase
  def setup
    @wheel = Wheel.new(26, 1.5)
  end

  def test_implements_the_diameterizable_interface
    assert_respond_to(@wheel, :diameter)
  end

  def test_calculates_diameter
    wheel = Wheel.new(26, 1.5)

    assert_in_delta(29, wheel.diameter, 0.01)
  end
end

class GearTest < Test::Unit::TestCase
  def test_calculates_gear_inches
    gear = Gear.new(
      chainring: 52,
      cog:       11,
      wheel:     Diameterizable.new
    )
    assert_in_delta(47.27, gear.gear_inches, 0.01)
  end
end
