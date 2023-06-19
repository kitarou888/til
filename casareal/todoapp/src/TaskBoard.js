import TaskList from "./TaskList";

const TaskBoard = (props) => {
  return (
    <div className="listsContainer">
      <TaskList title="やること" cards={props.cards} addCard={props.addCard} />
    </div>
  );
};

export default TaskBoard;
