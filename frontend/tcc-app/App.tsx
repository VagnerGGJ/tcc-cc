import React from "react";
import { PaperProvider } from "react-native-paper";
import RootNavigation from "./src/navigation/RootNavigation";
import "./src/styles/global.css";

export default function App() {
  return (
    <PaperProvider>
      <RootNavigation />
    </PaperProvider>
  );
}
