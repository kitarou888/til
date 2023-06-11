import React, { useEffect, useState } from "react";

const MAX_COUNT = 60;

const Timer = ({ maxCount = MAX_COUNT }) => {
  const [timeLeft, setTimeLeft] = useState(maxCount);
  const tick = () => {
    setTimeLeft((t) => t - 1);
  };
  const reset = () => setTimeLeft(maxCount);

  useEffect(() => {
    const timerId = setInterval(tick, 1000);
    return () => clearInterval(timerId);
  }, []);

  useEffect(() => {
    if (timeLeft === 0) setTimeLeft(maxCount);
    // if (timeLeft === 0) reset();
  });

  return (
    <>
      <div>Count</div>
      <div>{timeLeft}</div>
      <button onClick={reset}>reset</button>
    </>
  );
};

export default Timer;
