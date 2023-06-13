import TaskList from "./TaskList";

const TaskBoard = (props) => {
  return (
    <div className="listsContainer">
      <TaskList title="やること" cards={props.cards} />
    </div>
  );
};

export default TaskBoard;
