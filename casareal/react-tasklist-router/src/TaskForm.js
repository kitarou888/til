import { useState } from 'react';
import {
  Card,
  CardContent,
  CardActions,
  Button,
  TextareaAutosize,
} from '@mui/material';
import { styled } from '@mui/system';

const StyledButton = styled(Button)({
  color: 'white',
  backgroundColor: '#5aac44',
});

const StyledTextareaAutosize = styled(TextareaAutosize)({
  resize: 'none',
  outline: 'none',
  border: 'none',
  width: '100%',
});

const TaskForm = (props) => {
  const [text, setText] = useState('');

  const handleInputChange = (e) => {
    setText(e.target.value);
  };
  const handleAddCard = () => {
    alert('新しいカードを追加しました。');

  };
  return (
    <div>
      <Card>
        <CardContent>
          <StyledTextareaAutosize
            autoFocus
            onInput={handleInputChange}
          />
        </CardContent>
        <CardActions>
          <StyledButton
            onClick={handleAddCard}
            variant="contained"
          >
            カードの追加
          </StyledButton>
        </CardActions>
      </Card>
    </div>
  );
};

export default TaskForm;
