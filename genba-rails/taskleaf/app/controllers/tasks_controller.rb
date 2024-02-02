class TasksController < ApplicationController
  before_action :set_task, only: [:show, :edit, :update, :destroy]

  def index
    # @tasks = Task.all
    # @tasks = current_user.tasks.order(created_at: :desc)
    @q = current_user.tasks.ransack(params[:q])
    @tasks = @q.result(distinct: true)
  end

  def show
    # @task = Task.find(params[:id])
    # @task = current_user.find(params[:id])
  end

  def new
    @task = Task.new
  end

  def edit
    # @task = Task.find(params[:id])
    # @task = current_user.find(params[:id])
  end

  def update
    # task = Task.find(params[:id])
    # @task = current_user.find(params[:id])
    @task.update!(task_params)
    redirect_to tasks_url, notice: "タスク「#{@task.name}」を更新しました。"
  end

  def create
    # @task = Task.new(task_params)
    @task = current_user.tasks.new(task_params)

    if params[:back].present?
      render :new
      return
    end

    if @task.save
      TaskMailer.creation_email(@task).deliver_now
      redirect_to @task, notice: "タスク「#{@task.name}」を登録しました。"
    else
      render :new, status: :unprocessable_entity
    end
  end

  def destroy
    # task = Task.find(params[:id])
    # @task = current_user.find(params[:id])
    @task.destroy
    redirect_to tasks_url, notice: "タスク「#{@task.name}」を削除しました。"
  end

  def confirm_new
    @task = current_user.tasks.new(task_params)
    # render :confirm_new
    render :new, status: :unprocessable_entity unless @task.valid?
    # respond_to do |f|
    #   f.html { render :confirm_new }
    #   f.turbo_stream
    # end
    p "test"
    # render :confirm_new
  end

  private

  def task_params
    params.require(:task).permit(:name, :description)
  end

  def set_task
    @task = current_user.tasks.find(params[:id])
  end
end
