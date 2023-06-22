import { useParams } from "react-router-dom";

const ItemDetail = () => {
  const { pageno } = useParams();
  return <div>ページNo. {pageno}</div>;
};

export default ItemDetail;
