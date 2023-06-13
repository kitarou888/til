import "./App.css";

function App() {
  return (
    <div>
      <h1>TASK LIST</h1>
      <TaskBoard cards={cards} />
    </div>
  );
}

const cards = [
  { id: 1, body: "お茶を買う", category: "今日やること" },
  { id: 2, body: "牛乳を買う", category: "今日やること" },
  { id: 3, body: "あんぱんを買う", category: "今日やること" },
];

export default App;
