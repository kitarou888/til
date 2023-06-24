import React, { useState } from "react";
import Second from "./Second";
import Brother from "./Brother";

// TODO:コンテキストの用意
export const GreetingMessage = React.createContext();

const App = () => {
  // TODO：コンポーネント間で共有したいデータ
  const [greeting, setGreeting] = useState({ message: "はじめまして" });

  return (
    <div>
      <h1>第１階層コンポーネント:{greeting.message}</h1>
      {/* TODO：Providerコンポーネントでコンテキストを他のコンポーネントに供給 */}
      <GreetingMessage.Provider value={[greeting, setGreeting]}>
        <Second />
        <Brother />
      </GreetingMessage.Provider>
    </div>
  );
};

export default App;
