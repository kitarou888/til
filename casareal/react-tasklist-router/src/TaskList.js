import Paper from '@mui/material/Paper';
import { styled } from '@mui/system';
import TaskCard from './TaskCard';
import TaskForm from './TaskForm';

const StyledPaper = styled(Paper)({
  backgroundColor: '#ccc',
  height: '100%',
  width: 300,
  padding: 8,
  marginRight: 8,
});

// TaskListコンポーネント
export const TaskList = (props) => {

  const cardList = null;

  return (
    <StyledPaper>
      <h4>{props.title}</h4>
      {cardList ? (
        cardList.map((card) => {
          return <TaskCard key={card.id} card={card} />;
        })
      ) : (
        <div>カードなし</div>
      )}
      <TaskForm category={props.category} />
    </StyledPaper>
  );
};
export default TaskList;
