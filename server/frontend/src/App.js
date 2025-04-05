import LoginPanel from "./components/Login/Login";  
import Register from "./components/Register/Register"; // Importar el componente Register  
import { Routes, Route } from "react-router-dom";  

function App() {  
  return (  
    <Routes>  
      <Route path="/login" element={<LoginPanel />} />  
      <Route path="/register" element={<Register />} /> {/* Agregar la ruta de registro */}  
    </Routes>  
  );  
}  

export default App;  