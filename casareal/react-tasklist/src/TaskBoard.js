import { Box } from '@mui/material';
import { styled } from '@mui/system';
import TaskList from './TaskList';

const StyledBox = styled(Box)({
  display: 'flex',
  flexDirection: 'row',
});

const TaskBoard = () => {
  return (
    <StyledBox>
      <TaskList title="やること" category="今日やること" />
      <TaskList title="完了" category="完了したこと" />
    </StyledBox>
  );
};

export default TaskBoard;
