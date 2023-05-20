require 'minitest/autorun'
require_relative './gate'
require_relative './ticket'

class GateTest < Minitest::Test
  def test_from_umeda_to_juso_when_enough
    umeda = Gate.new(:umeda)
    juso = Gate.new(:juso)
    ticket = Ticket.new(160)
    umeda.enter(ticket)
    assert juso.exit(ticket)
  end

  def test_from_umeda_to_mikuni_when_not_enough
    umeda = Gate.new(:umeda)
    mikuni = Gate.new(:mikuni)
    ticket = Ticket.new(160)
    umeda.enter(ticket)
    refute mikuni.exit(ticket)
  end

  def test_from_umeda_to_mikuni_when_enough
    umeda = Gate.new(:umeda)
    mikuni = Gate.new(:mikuni)
    ticket = Ticket.new(190)
    umeda.enter(ticket)
    assert mikuni.exit(ticket)
  end

  def test_from_juso_to_mikuni_when_enough
    juso = Gate.new(:juso)
    mikuni = Gate.new(:mikuni)
    ticket = Ticket.new(160)
    juso.enter(ticket)
    assert mikuni.exit(ticket)
  end
end
