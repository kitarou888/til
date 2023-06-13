const TaskCard = ({ card }) => {
  return (
    <div className="cardContainer">
      <div>{card.body}</div>
    </div>
  );
};

export default TaskCard;
