module SomeFramework
  class Gear
    attr_reader :chainring, :cog, :wheel
    def initialize(chainring, cog, wheel)
      @chainring = chainring
      @cog = cog
      @wheel = wheel
    end
  end
end

# 外部のインターフェースをラップし、自身を変更から守る
module GearWrapper
  def self.gear(args)
    SomeFramework:: Gear.new(
      args[:chainring]
      args[:cog]
      args[:wheel]
    )
  end
end

# 引数を持つハッシュを渡すことでGearのインスタンスを作成できるように
GearWrapper.gear(
  :chainring => 52,
  :cog       => 11,
  :wheel     => Wheel.new(26, 1.5)
).gear_inches
