import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

import TaskBoard from './TaskBoard';
import LoginForm from './LoginForm';
import Home from './Home';
import ItemDetail from './ItemDetail';

// Appコンポーネント
const App = () => {
  return (
    <BrowserRouter>
      {/* ↑BrowserRouterコンポーネントによりルーティングを行う場として設定される */}
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">
            TASK LIST
          </Typography>
        </Toolbar>
      </AppBar>
      <div>
        {/* aタグを使う代わりにLinkタグを使ってリンクを設置 */}
        {/* to属性でこのリンクをクリックした際の遷移先URLを指定 */}
        <Link to="/home">[Home]</Link>
        <Link to="/board">[Board]</Link>
      </div>
      {/* Routesコンポーネントで、指定されたURLに合致する
      コンポーネントにページが切り替わるようにする */}
      <Routes>
        {/* Routeコンポーネントでルーティングの設定を行う */}
        <Route path="/home" element={<Home />} />
        <Route path="/board" element={<TaskBoard />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/detail/:pageno" element={<ItemDetail />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;