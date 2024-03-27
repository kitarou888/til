class Schedule
  def scheduled?(schedulable, start_date, end_date)
    puts "This #{schedulable.class} " +
      "is not scheduled¥n" +
      "  between #{start_date} and #{end_date}"
    false
  end
end

module Schedulable
  attr_writer :schedule

  def schedule
    @schedule ||= ::Schedule.new
  end

  def schedulable?(start_date, end_date)
    !scheduled?(start_date - lead_days, end_date)
  end

  def scheduled?(start_date, end_date)
    schedule.scheduled?(self, start_date, end_date)
  end

  # 必要に応じてインクルードする側で置き換える
  def lead_days
    0
  end
end

class Bicycle
  include Schedulable

  def lead_days
    1
  end

  def initialize(args={})
    @schedule = args[:schedule] || Schedule.new # Scheduleを注入し初期値を設定
    # @size = args[:size]
    # @chain = args[:chain] || default_chain
    # @tire_size = args[:tire_size] || default_tire_size

    # post_initialize(args) # Bicycleでは送信と・・・
  end

  # 与えられた期間の間、bicycleが利用可能であればtrueを返す
  def schedulable?(start_date, end_date)
    !scheduled?(start_date - lead_days, end_date)
  end

  # scheduleの答えを返す
  def scheduled?(start_date, end_date)
    schedule.scheduled?(self, start_date, end_date)
  end

  # bicycleがスケジュール可能となるまでの準備日数
  def lead_days
    1
  end

  def post_initialize(args) # ・・・実装の両方を行う
    nil
  end

  def spares
    { tire_size: tire_size,
      chain: chain }.merge(local_spares)
  end

  def local_spares # サブクラスがオーバーライドするためのフック
    {}
  end

  def default_chain # <- 共通の初期値
    '10-speed'
  end

  def default_tire_size
    raise NotImplementedError, "This #{self.class} cannot respond to:"
  end
end

require 'date'
starting = Date.parse("2015/09/04")
ending   = Date.parse("2015/09/10")

b = Bicycle.new
b.schedulable?(starting, ending)
