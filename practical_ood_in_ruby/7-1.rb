class Schedule
  def schefuled?(schedulable, start_date, end_date)
    puts "This #{schedulable.class} " +
      "is not scheduled¥n" +
      "  between #{start_date} and #{end_date}"
    false
  end
end
