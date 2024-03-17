class Trip
  attr_reader :bicycles, :customers, :vehicle
  # このmechanic引数はどんなクラスのものでもよい
  def prepare(mechanic)
    mechanic.prepare_bicycles(bicycles)
  end

  # ・・・
end

# このクラスのインスタンスを渡すことになったとしても動作する
class Mechanic
  def prepare_bicycles(bicycles)
    bicycles.each { |bicycle| prepare_bicycle(bicycle) }
  end

  def prepare_bicycle(bicycle)
    #...
  end
end
