import TaskCard from "./TaskCard";
import TaskForm from "./TaskForm";

const TaskList = (props) => {
  const handleTitleClick = () => {
    alert(props.title);
  };

  return (
    <div className="container">
      <h4 onClick={handleTitleClick}>{props.title}</h4>
      <div>カード枚数：{props.cards.length}枚</div>

      {props.cards.length ? (
        props.cards.map((card) => <TaskCard key={card.id} card={card} />)
      ) : (
        <div>カードなし</div>
      )}
      <TaskForm />
    </div>
  );
};

export default TaskList;
