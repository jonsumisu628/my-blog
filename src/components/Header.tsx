import React from "react";
import {
    AppBar,
    Toolbar,
    Typography,
    IconButton
} from "@material-ui/core";
import { AppBarProps } from "@material-ui/core/AppBar";
import { TypographyProps } from "@material-ui/core/Typography";
import { Menu as MenuIcon } from "@material-ui/icons";
import styled from "styled-components";

interface Props extends AppBarProps {
    toggleDrawer: () => void;
}

export default (
    {
        toggleDrawer,
        ...props
    }: Props
) => (
    <AppBar position="static" {...props}>
        <Toolbar>
            <IconButton
                color="inherit"
                aria-label="Menu"
                onClick={toggleDrawer}
            >
            <MenuIcon />
            </IconButton>
            <Title>ServiceName</Title>
        </Toolbar>
    </AppBar>
);

const Title = styled<TypographyProps>(Typography)`
    && {
        color: white;
        font-size: 1.5rem;
        letter-spacing: 2px;
    }
`;
