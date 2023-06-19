import { Paper, TextField, Typography, Button } from "@mui/material";
import { styled } from "@mui/system";

const StyledDiv = styled("div")({
  display: "flex",
  height: "100vh",
  backgroundColor: "#eeeeee",
});
const StyledPaper = styled(Paper)({
  width: "300px",
  height: "200px",
  margin: "auto",
  padding: "10px",
});
const StyledTextField = styled(TextField)({
  width: "80%",
});
const StyledButton = styled(Button)({
  margin: "15px",
});

const LoginForm = () => {
  return (
    <StyledDiv>
      <StyledPaper>
        <Typography>ログインしてください。</Typography>
        <StyledTextField label="Name" variant="standard"></StyledTextField>
        <StyledTextField label="Password" variant="standard"></StyledTextField>
        <StyledButton variant="contained" color="primary">
          ログイン
        </StyledButton>
      </StyledPaper>
    </StyledDiv>
  );
};

export default LoginForm;
