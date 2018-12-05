import React from "react";
import {
    withRouter,
    RouteComponentProps,
} from "react-router-dom";
import MainLayout, { MainLayoutEventProps }                 from "./components/wrappers/MainLayout";
import NotificationListener, { NotificationListenerProps }  from "./components/wrappers/NotificationListener";
import { PageComponentProps }                               from "./App";

// tslint:disable-next-line:max-line-length
export default withRouter<RouteComponentProps<any> & { children: React.ReactElement<any> }>((props: RouteComponentProps<any> & { children: React.ReactElement<PageComponentProps<any>> }) => (
    <NotificationListener
        // tslint:disable-next-line:jsx-no-lambda
        render={(notificationListener: NotificationListenerProps) =>
            <MainLayout
                render={(mainLayoutEventProps: MainLayoutEventProps) => React.cloneElement<PageComponentProps<any>>(
                    props.children,
                    {
                        ...mainLayoutEventProps,
                        ...notificationListener,
                        ...(
                            Object.entries(props)
                                .filter(x => x[0] !== "children")
                                .reduce((prev, next) => Object.assign(prev, { [next[0]]: next[1] }), {})
                        )
                    }
                )}
                {...notificationListener}
                {...props}
            />
        }
    />
));
