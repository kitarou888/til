import { useState, useEffect } from "react";

const TaskForm = (props) => {
  const [text, setText] = useState("");

  useEffect(() => {
    document.title = `入力文字数：${text.length}`;
    return () => {
      console.log(text.length * 2);
    };
  });

  useEffect(() => {
    const area = document.querySelector("textarea");
    area.style.backgroundColor = text.length > 5 ? "white" : "pink";
  }, [text]);

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  const handleAddCard = () => {
    props.addCard({ id: null, body: text, category: "今日やること" });
  };

  return (
    <div>
      <div>{text}</div>
      <div>
        <textarea className="editArea" onChange={handleInputChange} />
      </div>
      <div>
        <button onClick={handleAddCard}>カードの追加</button>
      </div>
    </div>
  );
};

export default TaskForm;
