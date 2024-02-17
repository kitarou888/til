class SampleJob < ApplicationJob
  queue_as :default

  def perform(*args)
    # Do something later
    # Sidekiq::Logging.logger.info "サンプルジョブを実行しましたよ"
    logger.info "サンプルジョブを実行しましたよ"
    logger.debug { "My args: #{args.inspect}" }
  end
end
