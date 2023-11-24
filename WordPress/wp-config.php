<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'n]zlswi8f%%a1G7s/4+1|L=/C<rZD+$;GI(+E3oY_w=jO3(]);fa`jM2Wb3Fr=wm' );
define( 'SECURE_AUTH_KEY',  'yaTMHe:m=3fADVm@io_Myjhy?4^},E]gxMPCW(Z{!3)D|4gqiUVu/uErk#ro[G77' );
define( 'LOGGED_IN_KEY',    'ymTYljXTx:4E[FL5Gt^xgjTIQ25j5v^~bVh{8$HbfvoJ1Duhc;W!.r-eq&RE$8O*' );
define( 'NONCE_KEY',        'A)5!$pFlsQ`oU7.[cr}Fq374& `ZvtkxW4EW/#@XvtH)@<q 19*rxc`7*sKz+p+u' );
define( 'AUTH_SALT',        '~#*jAwr(kgT#83P7I-ytI:TJ>VU3IR!CWv1ajB_:hrZ1 @3m-veURGoHKlB!2Dq]' );
define( 'SECURE_AUTH_SALT', '2[TjauX<Sb.U9RP^vm1+K3WW>9#{k{`Wj!RFFFJM0hI6k5({hcCm/uF><8m?]C&h' );
define( 'LOGGED_IN_SALT',   ')@]Rd4;?20@.*8/G<3N*uc{HKE}*J@bJ2aeym>}:5|aAa_4t=bDl4:a`G`T%Q+cR' );
define( 'NONCE_SALT',       '5=5.@)Qf{QD.fErLC?|*dk2iv|[xS_`:H/Wn.iHa76A(+H,GY%2faTAo.Atk2IFw' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
