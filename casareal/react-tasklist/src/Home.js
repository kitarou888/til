import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import Divider from '@mui/material/Divider';
import Icon from '@mui/material/Icon';
import { styled } from '@mui/system';
// TODO

const StyledBase = styled('div')({
  height: '100vh',
  padding: '20px',
  backgroundColor: '#ccc',
});
const StyledListRoot = styled('div')({
  width: '100%',
  maxWidth: 360,
  backgroundColor: 'white',
  boxShadow: '5px 5px rgba(0,0,0,0.5)',
});

const Home = () => {

  // TODO

  const handleClick = (event) => {
    // TODO

  };

  return (
    <StyledBase>
      <StyledListRoot>
        <List component="nav">
          <ListItem button component="a" href="/board">
            <ListItemIcon>
              <Icon>view_headline</Icon>
            </ListItemIcon>
            <ListItemText primary="ボード１" />
          </ListItem>
          <ListItem button>
            <ListItemIcon>
              <Icon>view_headline</Icon>
            </ListItemIcon>
            <ListItemText primary="ボード２" />
          </ListItem>
        </List>
        <Divider />
        <List component="nav">
          <ListItem button>
            <ListItemIcon>
              <Icon>settings</Icon>
            </ListItemIcon>
            <ListItemText primary="設定" />
          </ListItem>
          <ListItem button onClick={handleClick}>
            <ListItemIcon>
              <Icon>person</Icon>
            </ListItemIcon>
            <ListItemText primary="ログイン" />
          </ListItem>
        </List>
      </StyledListRoot>
    </StyledBase>
  );
};
export default Home;
