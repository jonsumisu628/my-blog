// import React    from "react";
// import Loadable from "react-loadable";

// const Loading = () => <div>Loading...</div>;

// export const DashboardPage = Loadable({
//     loader: () => import("./components/pages/DashboardPage"),
//     loading: Loading,
// });

// export const TopPage = Loadable({
//     loader: () => import("./components/pages/TopPage"),
//     loading: Loading,
// });

export { default as DashboardPage } from "./components/pages/DashboardPage";
export { default as TopPage      } from "./components/pages/TopPage";
