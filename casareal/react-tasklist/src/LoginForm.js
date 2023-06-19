import { Paper, TextField, Typography, Button } from "@mui/material";

const LoginForm = () => {
  return (
    <div>
      <Paper>
        <Typography>ログインしてください。</Typography>
        <TextField label="Name" variant="standard"></TextField>
        <TextField label="Password" variant="standard"></TextField>
      </Paper>
      <Button variant="contained" color="primary">
        ログイン
      </Button>
    </div>
  );
};

export default LoginForm;
