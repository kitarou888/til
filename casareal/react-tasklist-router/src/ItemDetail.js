import { useParams } from 'react-router-dom';

const ItemDetail = () => {
  // useParamsフック関数を呼び出し、パラメータを保持したオブジェクトを受け取る
  const { pageno } = useParams();
  return (
    <div>
      ページNo. {pageno}
    </div>
  );
};
export default ItemDetail;
