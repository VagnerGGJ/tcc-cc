import React from "react";
import { createDrawerNavigator } from "@react-navigation/drawer";
import HomeScreen from "../screens/HomeScreen";
import LoginScreen from "../screens/LoginScreen";
import ChatScreen from "../screens/ChatScreen";
import AdminScreen from "../screens/AdminScreen";
import WebViewScreen from "../screens/WebViewScreen";

export type DrawerParamList = {
    Home: undefined;
    Login: undefined;
    Chat: undefined;
    Admin: undefined;
    WebView: undefined;
};

const Drawer = createDrawerNavigator<DrawerParamList>();

export default function DrawerNavigation() {
    return (
        <Drawer.Navigator
            id={undefined}
            screenOptions={{
                headerShown: true,
            }}
        >
            <Drawer.Screen name="Home" component={HomeScreen} />
            <Drawer.Screen name="Login" component={LoginScreen} />
            <Drawer.Screen name="Chat" component={ChatScreen} />
            <Drawer.Screen name="Admin" component={AdminScreen} />
            <Drawer.Screen name="WebView" component={WebViewScreen} />
        </Drawer.Navigator>
    );
}
