import Paper from "@mui/material/Paper";
import { styled } from "@mui/system";
import TaskCard from "./TaskCard";
import TaskForm from "./TaskForm";

import { TaskCardsContext } from "./App";
import { useCallback, useContext } from "react";

const StyledPaper = styled(Paper)({
  backgroundColor: "#ccc",
  height: "100%",
  width: 300,
  padding: 8,
  marginRight: 8,
});

// TaskListコンポーネント
export const TaskList = (props) => {
  // カスタムフックで定義した状態取得用関数をコンテキストを通じて取得
  const { getCategorizedTaskCards } = useContext(TaskCardsContext);
  // カテゴリーを指定して対象のタスクカードだけを取り出す
  const cardList = getCategorizedTaskCards(props.category);

  return (
    <StyledPaper>
      <h4>{props.title}</h4>
      {cardList ? (
        cardList.map((card) => {
          return <TaskCard key={card.id} card={card} />;
        })
      ) : (
        <div>カードなし</div>
      )}
      <TaskForm category={props.category} />
    </StyledPaper>
  );
};
export default TaskList;
