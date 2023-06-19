//       ↓追記　 ↓追記     ↓追記
import { Paper, TextField, Typography, Button } from '@mui/material';
import { styled } from '@mui/system'; // ←追記

// ↓ここから追記
// スタイル付きコンポーネントを作成
const StyledDiv = styled('div')({
  display: 'flex',
  height: '100vh',
  backgroundColor: '#eeeeee',
});
const StyledPaper = styled(Paper)({
  width: '300px',
  height: '200px',
  margin: 'auto',
  padding: '10px',
});
const StyledTextField = styled(TextField)({
  width: '80%'
});
const StyledButton = styled(Button)({
  margin: '15px'
});
// ↑ここまで追記

// 修正：↓ JSX内でスタイル付きコンポーネントを配置
const LoginForm = () => {
  return (
    <StyledDiv>
      <StyledPaper>
        <Typography>ログインしてください。</Typography>
        <StyledTextField label="Name" variant="standard" />
        <StyledTextField label="Password" variant="standard" />
        <StyledButton
          variant="contained"
          color="primary"
        >
          ログイン
        </StyledButton>
      </StyledPaper>
    </StyledDiv>
  );
};
export default LoginForm;
