import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/system';

const StyledCard = styled(Card)({
  marginBottom: 10,
});

const TaskCard = (props) => {
  return (
    <StyledCard>
      <CardContent>
        <Typography>{props.card.body}</Typography>
      </CardContent>
    </StyledCard>
  );
};

export default TaskCard;
