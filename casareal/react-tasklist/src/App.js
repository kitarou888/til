import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import TaskBoard from "./TaskBoard";
import LoginForm from "./LoginForm";
import Home from "./Home";
import ItemDetail from "./ItemDetail";

const App = () => {
  return (
    <BrowserRouter>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">TASK LIST</Typography>
        </Toolbar>
      </AppBar>
      <div>
        <Link to="/home">[Home]</Link>
        <Link to="/board">[Board]</Link>
      </div>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/board" element={<TaskBoard />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/detail/:pageno" element={<ItemDetail />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
