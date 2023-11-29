Rails.application.routes.draw do
  get '/login', to: 'sessions#new'
  post '/login', to: 'sessions#create'
  delete '/logout', to: 'sessions#destroy'

  get 'sessions/new'
  namespace :admin do
    resources :users
  end

  resources :tasks
  root to: 'tasks#index'
  # controller :tasks do
  #   resources :tasks, only: [:index, :show]
  #   scope path: 's' do
  #     get 'task_contest', action: :edit
  #   end
  # end
end
