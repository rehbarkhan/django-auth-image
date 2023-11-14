import { Routes, Route } from "react-router-dom";
import MainRoute from "./Compoenents/MainRoute";
import AppPage from "./Pages/AppPage";
import NewVideo from "./Pages/NewVideo";

function App() {
  return (
    <Routes>
      <Route exact path="/app" element={<MainRoute />} >
        <Route index element={<AppPage />} />
        <Route path="upload" element={<NewVideo />} />
      </Route>
    </Routes>
  );
}

export default App;
