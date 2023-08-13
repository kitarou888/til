require 'minitest/autorun'
require_relative 'gate'

class GateTest < Minitest::Test
  def test_gate
    assert Gate.new
  end
end
