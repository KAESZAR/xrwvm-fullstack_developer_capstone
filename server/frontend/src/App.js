import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer";

function App() {
  return (
    <Routes>
            <Route path="/dealer/:id" element={<Dealer/>} />
            <Route path="/dealers" element={<Dealers/>} />
            <Route path="/login" element={<LoginPanel />} />
    </Routes>
  );
}
export default App;
