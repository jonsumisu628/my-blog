import React from "react";
import { PageComponentProps } from "../../App";
import Page                   from "../commons/Page";
import List                   from "@material-ui/core/List";
import ListItem               from "@material-ui/core/ListItem";
import ListItemText           from "@material-ui/core/ListItemText";
import ListItemAvatar         from "@material-ui/core/ListItemAvatar";
import Avatar                 from "@material-ui/core/Avatar";
import Typography             from "@material-ui/core/Typography";

export default class WorkListPage extends React.Component<PageComponentProps<{id: string}>>{

    render() {

        const {
            // history,
            // notificationListener
        } = this.props;

        return (
            <Page>
                TopPage
                <List>
                    <ListItem>
                        <ListItemAvatar>
                            <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
                        </ListItemAvatar>
                        <ListItemText
                            primary="Brunch this weekend?"
                            secondary={
                                <React.Fragment>
                                    <Typography component="span" color="textPrimary">
                                        Ali Connors
                                    </Typography>
                                    {" — I'll be in your neighborhood doing errands this…"}
                                </React.Fragment>
                            }
                        />
                    </ListItem>
                </List>
            </Page>
        );
    }
}
