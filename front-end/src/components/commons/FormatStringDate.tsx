import React from "react";

const dateToFormatString = (date: Date, fmt: string, locale: "ja-JP" | "en-US", pad?: string) => {
    const padding = (n: number, d: number, p?: string) => {
        const x = p || "0";
        return (x.repeat(d) + n).slice(-d);
    };
    const DEFAULT_LOCALE = "ja-JP";
    const getDataByLocale = (locale: "ja-JP" | "en-US", obj: any, param: number) => {
        const array = obj[locale] || obj[DEFAULT_LOCALE];
        return array[param];
    };
    const format = {
        YYYY: (_: "ja-JP" | "en-US") => padding(date.getFullYear(), 4, pad),
        YY  : (_: "ja-JP" | "en-US") => padding(date.getFullYear() % 100, 2, pad),
        MMMM: (locale: "ja-JP" | "en-US") =>
            getDataByLocale(
                locale,
                {
                    "ja-JP": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                    "en-US": ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"],
                },
                date.getMonth()
            )
        ,
        MMM : (locale: "ja-JP" | "en-US") =>
            getDataByLocale(
                locale,
                {
                    "ja-JP": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                    "en-US": ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                        "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."],
                },
                date.getMonth()
            )
        ,
        MM  : (_: "ja-JP" | "en-US") => padding(date.getMonth() + 1, 2, pad),
        M   : (_: "ja-JP" | "en-US") => date.getMonth() + 1,
        DD  : (_: "ja-JP" | "en-US") => padding(date.getDate(), 2, pad),
        D   : (_: "ja-JP" | "en-US") => date.getDate(),
        HH  : (_: "ja-JP" | "en-US") => padding(date.getHours(), 2, pad),
        H   : (_: "ja-JP" | "en-US") => date.getHours(),
        hh  : (_: "ja-JP" | "en-US") => padding(date.getHours() % 12, 2, pad),
        h   : (_: "ja-JP" | "en-US") => date.getHours() % 12,
        mm  : (_: "ja-JP" | "en-US") => padding(date.getMinutes(), 2, pad),
        m   : (_: "ja-JP" | "en-US") => date.getMinutes(),
        ss  : (_: "ja-JP" | "en-US") => padding(date.getSeconds(), 2, pad),
        s   : (_: "ja-JP" | "en-US") => date.getSeconds(),
        A   : (_: "ja-JP" | "en-US") => date.getHours() < 12 ? "AM" : "PM",
        a   : (locale: "ja-JP" | "en-US") =>
            getDataByLocale(
                locale, {
                    "ja-JP": ["午前", "午後"],
                    "en-US": ["am", "pm"],
                },
                date.getHours() < 12 ? 0 : 1
            )
        ,
        W   : (locale: "ja-JP" | "en-US") =>
            getDataByLocale(
                locale,
                {
                    "ja-JP": ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"],
                    "en-US": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                },
                date.getDay()
            )
        ,
        w   : (locale: "ja-JP" | "en-US") =>
            getDataByLocale(
                locale,
                {
                    "ja-JP": ["日", "月", "火", "水", "木", "金", "土"],
                    "en-US":  ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"],
                },
                date.getDay()
            )
    };
    const fmtstr = [""];
    Object.keys(format).forEach((key) =>
        fmtstr.push(key)
    );
    const re = new RegExp(`%(${fmtstr.join("|")})%`, "g");

    const replaceFn = (match: string, fmt: "YY" | "YYYY" | "YY" | "MMMM" | "MMM" | "MM" | "M" |
                                            "DD" | "D" | "HH" | "H" | "hh" | "h" | "mm" |
                                            "m" | "ss" | "s" | "A" | "a" | "W" | "w" | "") => {
        if (fmt === "")
            return "%";
        const func = format[fmt];

        if (func === undefined)
            return match;

        return func(locale);
    };

    return fmt.replace(re, replaceFn);
};

interface Props extends React.DetailedHTMLProps<React.HTMLAttributes<HTMLSpanElement>, HTMLSpanElement> {
    timestamp: number;
    format: string;
    isMillisec?: boolean;
    locale: "ja-JP" | "en-US";
    pad?: string;
}

export default (
    {
        timestamp,
        format,
        isMillisec = true,
        locale,
        pad,
        ...props
    }: Props
) => (
    <span
        {... props}
        unselectable={undefined}
    >
        {dateToFormatString(new Date(isMillisec ? timestamp : timestamp * 1000), format, locale, pad)}
    </span>
);
